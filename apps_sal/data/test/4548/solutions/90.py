(n, m, x) = list(map(int, input().split()))
am = list(map(int, input().split()))
list_n = [0] * n
for i in am:
    list_n[i - 1] = 1
print(min(sum(list_n[:x - 1]), sum(list_n[x - 1:])))
