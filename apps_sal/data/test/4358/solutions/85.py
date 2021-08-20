n = int(input())
al = [int(input()) for _ in range(n)]
mm = max(al)
print(sum(al) - mm // 2)
