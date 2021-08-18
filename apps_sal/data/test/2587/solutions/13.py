import sys
q = int(input())
for i in range(q):
    n = int(sys.stdin.readline())
    tak = (n * 4 - n) // 4
    print('9' * (tak) + '8' * (n - tak))
