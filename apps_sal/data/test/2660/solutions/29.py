import numpy as np
import heapq
Q = int(input())
Qinit = list(map(int, input().split()))
Qlist = [list(map(int, input().split())) for i in range(Q - 1)]

intercept = Qinit[2]
left_list = []
cent_list = [Qinit[1]]
right_list = []
left_sum = 0
right_sum = 0

median = Qinit[1]
count = 0

for query in Qlist:
    if query[0] == 1:
        source = query[1]
        intercept += query[2]

        if cent_list == []:
            if median > source:
                heapq.heappush(left_list, -source)
                left_sum += source
                tmp = -heapq.heappop(left_list)
                left_sum -= tmp
                cent_list.append(tmp)
            elif right_list[0] > source:
                cent_list.append(source)
            else:
                heapq.heappush(right_list, source)
                tmp = heapq.heappop(right_list)
                right_sum += source - tmp
                cent_list.append(tmp)
            median = cent_list[0]
        else:
            if cent_list[0] < source:
                heapq.heappush(left_list, -cent_list[0])
                left_sum += cent_list[0]
                median = cent_list[0]
                heapq.heappush(right_list, source)
                right_sum += source
                cent_list.remove(cent_list[0])
            else:
                heapq.heappush(left_list, -source)
                left_sum += source
                median = -left_list[0]
                heapq.heappush(right_list, cent_list[0])
                right_sum += cent_list[0]
                cent_list.remove(cent_list[0])
            count += 1

    else:
        minval = np.abs(left_sum - count * median) + np.abs(right_sum - count * median) + intercept
        print(("{} {}".format(median, minval)))
