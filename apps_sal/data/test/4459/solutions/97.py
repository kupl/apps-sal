from collections import Counter
input();print(sum(j if i>j else j-i for i,j in Counter(map(int,input().split())).items()))
