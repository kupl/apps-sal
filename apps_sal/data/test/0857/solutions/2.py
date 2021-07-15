n, m = [int(v) for v in input().split()]
x = [int(v) for v in input().split()]
y = {int(v) for v in input().split()}

print(' '.join(str(v) for v in x if v in y))

