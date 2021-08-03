N = int(input())
li = [0, 0, 0, 0, 0]
for i in range(5):
    li[i] = int(input())

if N % min(li) == 0:
    a = N // min(li) - 1
else:
    a = N // min(li)
ans = 5 + a

print(ans)
