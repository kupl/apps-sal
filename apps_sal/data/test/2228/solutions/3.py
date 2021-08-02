from sys import stdin


def input():
    return stdin.readline().strip()


n = int(input())
birth_arr = []
death_arr = []
for i in range(n):
    b, d = list(map(int, input().split()))
    birth_arr.append(b)
    death_arr.append(d)

birth_arr = sorted(birth_arr)
death_arr = sorted(death_arr)

num_ppl = len(birth_arr)
curr = 0
curr_year = 0
max_year = None
max_ppl = 0
b_pointer = 0
d_pointer = 0

while b_pointer < num_ppl:
    if birth_arr[b_pointer] < death_arr[d_pointer]:
        curr += 1
        curr_year = birth_arr[b_pointer]
        if curr > max_ppl:
            max_year = curr_year
            max_ppl = curr
        b_pointer += 1
    elif birth_arr[b_pointer] == death_arr[d_pointer]:
        curr_year = birth_arr[b_pointer]
        b_pointer += 1
        d_pointer += 1
    else:
        curr -= 1
        curr_year = death_arr[d_pointer]
        d_pointer += 1

print(f"{max_year} {max_ppl}")
