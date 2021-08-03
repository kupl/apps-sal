from collections import defaultdict
mediana = input().split()
seq = input().split()
index = result = cnt = 0
hashmap = defaultdict(lambda: 0)
while (mediana[1] != seq[index]):
    index += 1
hashmap[0] = 1
for i in range(index + 1, int(mediana[0])):
    if (int(seq[i]) > int(mediana[1])):
        cnt += 1
    else:
        cnt -= 1
    hashmap[cnt] += 1
cnt = 0
for i in range(index - 1, -1, -1):
    if (int(seq[i]) < int(mediana[1])):
        cnt += 1
    else:
        cnt -= 1
    result += hashmap[cnt]
    result += hashmap[cnt + 1]
result += hashmap[0] + hashmap[1]
print(result)
