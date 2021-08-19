def multiple_of_nine():
    N = int(input())
    if N % 9 == 0:
        return 'Yes'
    else:
        return 'No'


result = multiple_of_nine()
print(result)
