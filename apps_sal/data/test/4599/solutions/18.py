import sys
lines = [s.rstrip('\n') for s in sys.stdin.readlines()]
(n,) = [int(num) for num in lines.pop(0).split(' ')]
a_list = [int(num) for num in lines.pop(0).split(' ')]
a_list.sort(reverse=True)
alice_sum = sum((a_list[i] for i in range(0, n, 2)))
bob_sum = sum(a_list) - alice_sum
print(alice_sum - bob_sum)
