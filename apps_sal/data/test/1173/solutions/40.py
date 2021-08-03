import sys

N = int(input())
amat = [[-1]]
for i in range(N):
    alist = list(map(int, input().split()))
    amat.append(list(reversed(alist)))

# print(amat)
cleared_num = 0
new_search_index = set(range(1, N + 1))
for answer in range(1, N**3):
    matched_set = set()
    unchanged = True

    search_index = new_search_index
    new_search_index = set()
    for i in search_index:
        if i in matched_set:
            continue

        ai_next = amat[i][-1]
        if amat[ai_next][-1] == i and not ai_next in matched_set:
            # print(i,ai_next,answer)
            matched_set.add(amat[i].pop())
            matched_set.add(amat[ai_next].pop())
            if len(amat[i]) == 0:
                cleared_num += 1
            else:
                new_search_index.add(i)
            if len(amat[ai_next]) == 0:
                cleared_num += 1
            else:
                new_search_index.add(ai_next)
            unchanged = False

    if unchanged:
        print(-1)
        return
    elif cleared_num == N:
        print(answer)
        return
