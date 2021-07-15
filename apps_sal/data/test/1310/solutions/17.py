import itertools
import functools
def allSubArrays(xs):
    n = len(xs)
    indices = list(range(n+1))
    for i,j in itertools.combinations(indices,2):
        yield xs[i:j]
n=int(input())
my_list=list(map(int,input().split(" ")))
list_=list(allSubArrays(my_list))
for i in range(len(list_)):
    list_[i]=functools.reduce(lambda x,y:x^y,list_[i])
print(max(list_))

