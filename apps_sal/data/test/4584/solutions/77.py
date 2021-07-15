N = int(input())
hie_list = list(map(int, input().split()))

hie_dic = {}

for i in range(N - 1):
    hie_dic[i + 1] = 0
    hie_dic[hie_list[i]] += 1

for i in range(N - 1):
    print(hie_dic[i + 1])
print(0)
