n = int(input())
our_list_1 = list(map(int, input().split()))
our_list_2 = []
for i in range(n):
    our_list_2.append(sum(list(map(int, input().split()))))
our_sum = our_list_2[0] * 5 + 15 * our_list_1[0]
for i in range(n):
    if (our_list_2[i] * 5 + 15 * our_list_1[i]) < our_sum:
        our_sum = ( our_list_2[i] * 5 + 15 * our_list_1[i])
print(our_sum)    
