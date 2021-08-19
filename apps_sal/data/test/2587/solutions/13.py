import sys
# q=2
q = int(input())
for i in range(q):
    #n,k,z=[int(j) for j in sys.stdin.readline().split()]
    n = int(sys.stdin.readline())
    #a=[int(j) for j in sys.stdin.readline().split()]
    # a=sys.stdin.readline().strip()
    tak = (n * 4 - n) // 4
    print('9' * (tak) + '8' * (n - tak))
