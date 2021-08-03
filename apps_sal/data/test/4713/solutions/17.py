N = int(input())
S = input()

ans = 0
highest = 0
for i in S:
    if i == "I":
        ans += 1
    else:
        ans -= 1
    if highest <= ans:
        highest = ans

print(highest)
