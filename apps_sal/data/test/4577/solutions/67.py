(A, B, C) = map(int, input().split())
if -100 <= A and B and (C <= 100):
    if C >= A and C <= B:
        print('Yes')
    else:
        print('No')
