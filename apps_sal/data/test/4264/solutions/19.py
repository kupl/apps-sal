N = int(input())
ii = 0
for i in range(1,N+1):
    s = str(i)
    if len(s) % 2 == 1:
        ii += 1
print(ii)
