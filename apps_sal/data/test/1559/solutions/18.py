import math  # , time

l = int(input())
a = input()

#t_s = time.time()
#log = int(math.log10(a))+1

l_a = len(a)
# print(l_a)


if((l_a % l) != 0):
    l_in_P = int(l_a / l) + 1
    i = 0
    P = (10 ** (l - 1))
    P = str(P)
    amount = 0
    while(i < l_in_P):
        print(P, end='')
        i = i + 1

else:

    l_in_P = int(l_a / l)
    #print('l_in_P=', l_in_P)
    # print(l_in_P)

    #a_str = str(a)
    a_str = a
    int_for_P = a_str[0:l]

    compare = '='
    i = 0
    while(i < l_in_P):
        index = l * i
        #j = 0
        # while(j<l):
        # if( int(a_str[index+j]) != int(int_for_P[j]) ) :
        # if(int(a_str[index+j]) < int(int_for_P[j])) :
        #compare = '<'
        # else:
        #compare = '>'
        # break
        #j = j + 1
        #print(a_str[index:(index+l)],'int_for_P',int_for_P, i)
        difference = int(a_str[index:(index + l)]) - int(int_for_P)
        if(difference != 0):
            if(difference < 0):
                compare = '<'
            else:
                compare = '>'
            break

        # if (compare != '='):
            # break
        i = i + 1

    if(compare == '<'):
        #int_for_P = str(int_for_P)
        i = 0
        while(i < l_in_P):
            print(int_for_P, end='')
            i = i + 1
    else:
        #P = int(int_for_P) + 1
        #exam_length_P = int(math.log10(P))+1
        #exam_length_P = len(str(P))
        if(int_for_P != ('9' * l)):
            #P = str(P)
            P = int_for_P
            k = l - 1
            while(P[k] == '9'):
                k = k - 1

            P = P[0:(k)] + str(int(P[k]) + 1) + ('0' * (l - k - 1))

            i = 0
            while(i < l_in_P):
                print(P, end='')
                i = i + 1
        else:
            #P = 10 ** (l - 1)
            P = '1' + '0' * (l - 1)
            l_in_P = l_in_P + 1
            # print('l_inP=',l_in_P)
            i = 0
            while (i < l_in_P):
                print(P, end='')
                i = i + 1
#t_f = time.time()
# print('')
# print(t_f-t_s)
