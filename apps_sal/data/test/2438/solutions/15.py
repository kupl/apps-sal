n = int(input())
s = input()

prev_b = -1
prev_a = -1
ans = 0
for i in range(n):
    if s[i] == "B":
        ans += prev_b + 1
        if prev_b + 1 == i and prev_a != -1:
            ans -= 1
        prev_b = i 
        
    else:
        ans += prev_a + 1
        if prev_a + 1 == i and prev_b != -1:
            ans -= 1
        prev_a = i
print(ans)
