import itertools

n, m = map(int, input().split())

#繋がっている頂点リスト
a_list = []
for j in range(m) :
    a = list(map(int, input().split()))
    a_list.append(a)
a_list.sort()

#道順リスト(最初が1に限る)
b_list = [k for k in itertools.permutations([l for l in range(1, n + 1)]) if k[0] == 1]

#道順リストの中で頂点リストが含まれているもの
cnt = 0
for x in b_list :
    tf_list = []
    for y in range(n - 1) :
        tf_list.append([x[y], x[y + 1]] in a_list or [x[y + 1], x[y]] in a_list)
    
    if all(tf_list) == True :
        cnt += 1

print(cnt)
