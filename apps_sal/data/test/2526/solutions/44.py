(x, y, a, b, c) = list(map(int, input().split()))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
p = p[:x]
q = q[:y]
eat = p + q + r
eat.sort(reverse=True)
eat = eat[:x + y]
print(sum(eat))
