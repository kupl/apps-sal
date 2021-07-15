n, m = list(map(int, input().split()))
our_list = list(map(int, input().split()))
our_list_2 = []
for i in range(n + 1):
    our_list_2.append(0)
for i in range(m):
    for j in range(our_list[i], n + 1):
        if our_list_2[j] == 0:
            our_list_2[j] = our_list[i]
print(' '.join(list(map(str, our_list_2[1:]))))

