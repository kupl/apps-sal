rating = int(input())

if rating < 1200:
    print('ABC')
elif 1200 <= rating < 2800:
    print('ARC')
elif rating >= 2800:
    print('AGC')
