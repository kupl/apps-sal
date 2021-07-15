class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        len_str1 = len(str1)
        len_str2 = len(str2)
        matrix = [[[0, ''] for x in range(len_str1)] for y in range(len_str2)]
        for i in range(len_str2):
            for k in range(len_str1):
                if(i == 0 and k == 0):
                    if(str1[0] == str2[0]):
                        matrix[i][k] = [1, 'D']
                elif(i == 0):
                    if(str2[i] == str1[k]):
                        matrix[i][k] = [1, 'D']
                    else:
                        matrix[i][k] = [matrix[i][k-1][0], 'L']
                elif(k == 0):
                    if(str2[i] == str1[k]):
                        matrix[i][k] = [1, 'D']
                    else:
                        matrix[i][k] = [matrix[i-1][k][0], 'U']
                else:
                    if(str2[i] == str1[k]):
                        matrix[i][k] = [matrix[i-1][k-1][0]+1, 'D']
                    else:
                        if(matrix[i][k-1][0] > matrix[i-1][k][0]):
                            matrix[i][k] = [matrix[i][k-1][0], 'L']
                        else:
                            matrix[i][k] = [matrix[i-1][k][0], 'R']
        if(matrix[-1][-1] == 0):
            return str1+str2
        str1_lis, str2_lis = [], []
        str_val = ''
        val = matrix[-1][-1][0]
        i, k = len_str2-1, len_str1-1
        while(val > 0):
            if(matrix[i][k][1] == 'D'):
                val -= 1
                str_val += str2[i]
                str1_lis.append(k)
                str2_lis.append(i)
                i -= 1
                k -= 1
            elif(matrix[i][k][1] == 'L'):
                k -= 1
            else:
                i -= 1
        #for i in matrix:
        #    print(i)
        str_val = str_val[::-1]
        str1_lis = str1_lis[::-1]
        str2_lis = str2_lis[::-1]
        #print(str_val, str1_lis, str2_lis)
        final_str = str1[:str1_lis[0]] + str2[:str2_lis[0]] + str_val[0]
        for i in range(1, len(str_val)):
            final_str += str1[str1_lis[i-1]+1:str1_lis[i]] + str2[str2_lis[i-1]+1:str2_lis[i]] + str_val[i]
        if(str1_lis[-1] < len_str1-1):
            final_str += str1[str1_lis[-1]+1:]
        if(str2_lis[-1] < len_str2-1):
            final_str += str2[str2_lis[-1]+1:]
        return final_str
