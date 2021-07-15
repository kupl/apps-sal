'''
Based on solution from Firepaw which is awesome
'''

k1 = 0


def main():
    n, k = [int(x) for x in input().split()]
    if k & 1 == 0 or k > 2*n-1:
        print("-1")
    else:
        lst = [0]*n

        # k1 count how many recursions left, drain one for the initial  call
        nonlocal k1
        k1 = k - 1

        # solve the task for [l, r)
        # Filling array with values val, val+1, ...
        def fill_arr(l, r, val):
            nonlocal k1
            # list size 1, nothing to do just set the value
            if r <= l+1:
                lst[l] = val
            elif k1 == 0:
                # just fill in a sorted array - no more calls here
                for i in range(l, r):
                    lst[i] = val + i - l
            else:
                # drain 2 recursion calls (for left and right path)
                k1 -= 2
                # call subproblems
                m = (l+r) // 2
                # set initial vals for left path as [val + r-m, ... , val + r)
                fill_arr(l, m, val+r-m)

                # set initial vals for right path as [val, val+1, ... , val + r-m)
                fill_arr(m, r, val)

                # after filling subproblems we are sure list is not sorted
                # this justifies the draining k1

        fill_arr(0, n, 1)
        #assert(k1 == 0)
        print(" ".join(map(str, lst)))


def __starting_point():
    main()

__starting_point()
