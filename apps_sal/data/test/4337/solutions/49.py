N = int(input())
S = list(map(str, input().split()))

# 黄色'Y'が入っていなければ、Three

if 'Y' not in S:
    print('Three')
else:
    print('Four')
