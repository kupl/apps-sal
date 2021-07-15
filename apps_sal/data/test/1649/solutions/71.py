
a, b, c, d = map(int, input().split())

s_ = a + b + c + d

ans = 'No'

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                if s_ - (a * i + b * j + c * k + d * l) == (a * i + b * j + c * k + d * l):
                    ans = 'Yes'


print(ans)
