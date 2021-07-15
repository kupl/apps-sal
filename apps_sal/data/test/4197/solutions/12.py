n = int(input())
a = [int(i) for i in input().split()]
lst = [0 for _ in range(n)]
i = 1
for ai in a:
  lst[ai-1] = i
  i += 1
print(' '.join([str(i) for i in lst]))
