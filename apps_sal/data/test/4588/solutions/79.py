(A, B) = input().split()
mydict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
print('>') if mydict[A] > mydict[B] else print('<') if mydict[A] < mydict[B] else print('=')
