n = int(input())
com = input()
print(min(com.count('L'), com.count('R')) * 2 + min(com.count('U'), com.count('D')) * 2)
