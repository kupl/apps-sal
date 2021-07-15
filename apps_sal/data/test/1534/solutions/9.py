s = input()
size = len(s)
a = [0]*(size+1)
b = [0]*(size+1)
for i in range(size):
    a[i+1] = a[i] + (1 if s[i] == 'a' else 0)
    b[i+1] = b[i] + (1 if s[i] == 'b' else 0)
ans = 0
for i in range(size+1):
    for j in range(i+1):
        val = b[i] - b[j] + a[j] + a[size] - a[i]
        ans = max(val,ans)
print(ans)

