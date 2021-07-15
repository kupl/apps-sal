n = int(input())
# cs = ['W' for i in range(200000)]
cs = input()

w_count = 0
for c in cs:
    if c == 'W':
        w_count += 1

if w_count == 0:
    print((0))
    return

rest = cs[-w_count:]

answer = 0
for c in rest:
    if c == 'R':
        answer += 1
print(answer)

