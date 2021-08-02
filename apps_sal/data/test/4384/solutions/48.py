contest_num = int(input())

if contest_num >= 1999:
    result_str = 'The contest has not been held'

elif contest_num < 1000:
    result_str = 'ABC'

elif contest_num >= 1000:
    result_str = 'ABD'

print(result_str)
