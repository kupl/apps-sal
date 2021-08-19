n = int(input())
x = map(int, input().split())
(k, res) = (0, 0)
for elm in x:
    if elm != -1:
        k += elm
        continue
    if elm == -1 and k > 0:
        k -= 1
    else:
        res += 1
print(res)
