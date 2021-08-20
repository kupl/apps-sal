n = int(input())
a = list(map(int, input().split()))
print('First' if any([ai % 2 == 1 for ai in a]) else 'Second')
