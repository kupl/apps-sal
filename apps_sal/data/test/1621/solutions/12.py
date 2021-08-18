string = str(input())

k = int(input())

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


dic = {}
for count, x in enumerate(str(input()).split(" ")):
    dic.update({alphabet[count]: int(x)})

max_w = max(dic.values())

all_sum = 0
for count, sym in enumerate(string):
    all_sum += (count + 1) * dic[str(sym)]

for new in range(len(string) + 1, len(string) + k + 1):
    all_sum += new * max_w

print(all_sum)
