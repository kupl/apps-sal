N = int(input())
S = list(map(str, input().split()))
if 'P' in S and 'W' in S and ('G' in S) and ('Y' in S):
    print('Four')
else:
    print('Three')
