class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        p1 = [p1[0] * 4, p1[1] * 4]
        p2 = [p2[0] * 4, p2[1] * 4]
        p3 = [p3[0] * 4, p3[1] * 4]

        p4 = [p4[0] * 4, p4[1] * 4]

        center_x = (p1[0] + p2[0] + p3[0] + p4[0]) / 4
        center_y = (p1[1] + p2[1] + p3[1] + p4[1]) / 4
        print((center_x, " ", center_y))

        # if center_x != center_y:
        # return False
        #print(center_x, " ", center_y)

        if p1 == [center_x, center_y]:
            return False

        #print(center_x, " ", center_y)

        center_to_p1 = [center_x - p1[0], center_y - p1[1]]
        e_p2 = [(int)(center_x - (center_y - p1[1])), (int)(center_y + (center_x - p1[0]))]
        e_p3 = [(int)(center_x + center_x - p1[0]), (int)(center_y + center_y - p1[1])]
        e_p4 = [(int)(center_x + (center_y - p1[1])), (int)(center_y - (center_x - p1[0]))]

        #print ("e_p2 ", e_p2, " e_p3 ", e_p3, " e_p4 ", e_p4)

        #print ("p2 ", p2, " p3 ", p3, " p4 ", p4)

        if (e_p2 == p2 or e_p2 == p3 or e_p2 == p4) and (e_p3 == p2 or e_p3 == p3 or e_p3 == p4) and (e_p4 == p2 or e_p4 == p3 or e_p4 == p4):
            return True
        else:
            return False
