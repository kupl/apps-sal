(n, m, minimum, maximum) = list(map(int, input().split()))
list_of_m = list(map(int, input().split()))
maxi = max(list_of_m)
mini = min(list_of_m)
if maxi < maximum and mini > minimum:
    if n - m >= 2:
        print('Correct')
    else:
        print('Incorrect')
elif maxi == maximum and mini > minimum:
    if n - m >= 1:
        print('Correct')
    else:
        print('Incorrect')
elif maxi < maximum and mini == minimum:
    if n - m >= 1:
        print('Correct')
    else:
        print('Incorrect')
elif maxi == maximum and mini == minimum:
    print('Correct')
else:
    print('Incorrect')
