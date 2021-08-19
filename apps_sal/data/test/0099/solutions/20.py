x = list(map(int, input().split()))
init_term = x[0]
ratio = x[1]
abs_max = x[2]
num_bad = x[3]

bad_list = list(map(int, input().split()))

curr_val = 0
curr_val += init_term
num_to_write = 0

if abs(init_term) > abs_max:
    print("0")
else:
    if init_term == 0:
        if init_term in bad_list:
            print("0")
        else:
            print("inf")  # minimum abs_max can be is 1.
    else:
        if ratio == 1:
            if (curr_val * ratio in bad_list):
                print("0")
            else:
                print("inf")

        elif ratio == 0:
            if (0 in bad_list and init_term in bad_list):
                print("0")
            elif 0 in bad_list:
                print("1")
            else:
                print("inf")

        elif ratio == -1:
            if (init_term in bad_list and -init_term in bad_list):
                print("0")

            else:
                print("inf")

        else:
            while (abs(curr_val) <= abs_max):
                if curr_val not in bad_list:
                    num_to_write += 1
                curr_val *= ratio

            print(num_to_write)
