a, ta = list(map(int, input().split(' ')))
b, tb = list(map(int, input().split(' ')))
depart = tuple(map(int, input().split(':')))


depart_t = 60 * depart[0] + depart[1]

arrival = depart_t + ta


count = 0

ct = 5 * 60
while ct < arrival and ct < 24 * 60:
    if ct > depart_t - tb:
        count += 1
    ct += b

print(count)
