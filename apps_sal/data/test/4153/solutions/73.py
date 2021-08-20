from collections import Counter
num_dict = Counter(input())
if num_dict.get('0') is not None and num_dict.get('1') is not None:
    if num_dict.get('0') > num_dict.get('1'):
        print(num_dict.get('1') * 2)
    else:
        print(num_dict.get('0') * 2)
else:
    print(0)
