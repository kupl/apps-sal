I = [int(i) for i in input().split()]
(conf, friend) = (I[0], I[1])
answer = []
ans = ''
mod = conf % friend
for i in range(friend):
    answer.append(int((conf - mod) / friend))
for i in range(mod):
    answer[i] += 1
for i in range(friend):
    ans += str(answer[i]) + ' '
print(ans[:-1])
