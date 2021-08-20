x = int(input())
(ans, k, i) = (0, 1, 0)
while 1:
    ans += k
    if ans >= x:
        break
    k += 1
print(k)
