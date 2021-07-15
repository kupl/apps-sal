h, a = [int(i) for i in input().split()]
ans = h // a if h % a == 0 else h // a + 1
print(ans)
