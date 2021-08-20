(x, t) = map(int, input().split())
answer = x - t
if answer <= -1:
    print(0)
else:
    print(answer)
