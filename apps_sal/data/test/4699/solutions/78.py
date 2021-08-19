(n, k) = list(map(int, input().split()))
d = list(map(int, input().split()))
s = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} - set(str(d))
ans = n
while (s >= set(str(n))) == False:
    n += 1
    if (s >= set(str(n))) == True:
        ans = n
        break
print(ans)
