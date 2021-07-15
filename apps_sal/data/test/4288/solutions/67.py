a, b, c = [int(i) for i in input().split()]
print('Yes' if len(set([a, b, c])) == 2 else 'No') 
