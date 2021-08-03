N = int(input())

i = 1
lst = []
while i * i <= N:
    if N % i == 0:
        lst.append(max(i, N // i))
    i += 1

ans = min(lst)
print(len(str(ans)))
