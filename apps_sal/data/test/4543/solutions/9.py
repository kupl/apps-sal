num = int(''.join(input().split()))
root = num ** 0.5
print('Yes' if root.is_integer() else 'No')
