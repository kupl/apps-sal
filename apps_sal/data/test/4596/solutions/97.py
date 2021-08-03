n = int(input())
n_list = list(map(int, input().split()))
count = 0


def check(list):
    for i in range(n):
        if(n_list[i] % 2 != 0):
            return False
    return True


while(check(n_list)):
    n_list = [k / 2 for k in n_list]
    count += 1
print(count)
