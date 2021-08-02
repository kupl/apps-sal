from heapq import heappush, heappop


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

all_freq = {}

cnt_b = [0] * 220000
for num in b: cnt_b[num] += 1


for num in a:
    if num not in all_freq:
        all_freq[num] = 0
    all_freq[num] += 1

for num in b:
    if num not in all_freq:
        all_freq[num] = 0
    all_freq[num] += 1

heap = []

for num, freq in list(all_freq.items()):
    if freq > n:
        print("No")
        return
    if cnt_b[num] > 0:
        heappush(heap, (-freq, num))

ans = []


def get_max():
    (freq, num) = heappop(heap)
    freq = -freq
    while all_freq[num] != freq:
        (freq, num) = heappop(heap)
        freq = -freq

    return num


for num in a:
    most_freq_num = get_max()
    if most_freq_num != num:
        ans.append(most_freq_num)
        all_freq[most_freq_num] -= 1
        cnt_b[most_freq_num] -= 1
        if cnt_b[most_freq_num] > 0:
            heappush(heap, (-all_freq[most_freq_num], most_freq_num))
    else:
        second_freq_num = get_max()
        heappush(heap, (-all_freq[most_freq_num], most_freq_num))
        ans.append(second_freq_num)
        all_freq[second_freq_num] -= 1
        cnt_b[second_freq_num] -= 1
        if cnt_b[second_freq_num] > 0:
            heappush(heap, (-all_freq[second_freq_num], second_freq_num))
    all_freq[num] -= 1
    if cnt_b[num] == 0: continue
    heappush(heap, (-all_freq[num], num))

print("Yes")
print((*ans))
